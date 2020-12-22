#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import sys
import signal
import threading
import ctypes

from core.exceptions import exceptions
from core.badges import badges
from core.storage import storage
from core.io import io

class jobs():
    def __init__(self):
        self.exceptions = exceptions()
        self.badges = badges()
        self.storage = storage()
        self.io = io()

        self.job_process = None

    def exit_jobs(self):
        if not self.storage.get("jobs"):
            return True
        else:
            self.badges.output_warning("You have some running jobs:")
            for job in self.storage.get("jobs").keys():
                self.io.output("    " + job)
            state = self.badges.input_confirm("Exit anyway? [y/N] ").lower()
            if state  == "y" or state == "yes":
                self.badges.output_process("Stopping all jobs...")
                self.stop_all_jobs()
                return True
        return False

    def stop_all_jobs(self):
        for job in list(self.storage.get("jobs").keys()):
            self.delete_job(job)

    def stop_job(self, job):
        thread = job
        if not thread.is_alive():
            raise self.exceptions.GlobalException
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
        if res == 0:
            raise self.exceptions.GlobalException
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
            raise self.exceptions.GlobalException

    def start_job(self, job_function, job_arguments):
        self.job_process = threading.Thread(target=job_function, args=job_arguments)
        self.job_process.setDaemon(False)
        self.job_process.start()

    def delete_job(self, job_name):
        if job_name in list(self.storage.get("jobs").keys()):
            for module_category in list(self.storage.get("jobs")[job_name].keys()):
                for module_name in list(self.storage.get("jobs")[job_name][module_category].keys()):
                    try:
                        self.stop_job(self.storage.get("jobs")[job_name][module_category][module_name])
                    except:
                        pass
                    if hasattr(self.storage.get("modules")[module_category][module_category + '/' + module_name], "finish"):
                        self.storage.get("modules")[module_category][module_category + '/' + module_name].finish()
                    self.storage.delete_element("jobs", job_name)
        else:
            self.badges.output_error("Failed to stop job!")
            raise self.exceptions.GlobalException

    def create_job(self, job_name, job_function, job_arguments, module_category, module_name):
        self.start_job(job_function, job_arguments)
        if not self.storage.get("jobs"):
            self.storage.set("jobs", {job_name:{module_category:{module_name:self.job_process}}})
        else:
            self.storage.update("jobs", {job_name:{module_category:{module_name:self.job_process}}})