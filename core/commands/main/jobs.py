#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2021 EntySec
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

from core.io import io
from core.jobs import jobs
from core.badges import badges
from core.storage import storage
from core.formatter import formatter

class ZetaSploitCommand:
    def __init__(self):
        self.io = io()
        self.jobs = jobs()
        self.badges = badges()
        self.storage = storage()
        self.formatter = formatter()

        self.details = {
            'Category': "jobs",
            'Name': "jobs",
            'Description': "Manage active jobs.",
            'Usage': "jobs [-l|-k <id>]",
            'ArgsCount': 1,
            'NeedsArgs': True,
            'Args': list()
        }

    def run(self):
        choice = self.details['Args'][0]
        self.jobs.remove_dead()
        if choice == '-l':
            if self.storage.get("jobs"):
                jobs_data = list()
                headers = ("ID", "Name", "Module")
                jobs = self.storage.get("jobs")
                for job_id in jobs.keys():
                    jobs_data.append((job_id, jobs[job_id]['job_name'], jobs[job_id]['module_name']))
                self.io.output("")
                self.formatter.format_table("Active Jobs", headers, *jobs_data)
                self.io.output("")
            else:
                self.badges.output_warning("No running jobs available!")
        elif choice == '-k':
            if len(self.details['Args']) < 2:
                self.io.output(self.details['Usage'])
            else:
                try:
                    self.jobs.delete_job(self.details['Args'][1])
                except Exception:
                    pass
        else:
            self.io.output(self.details['Usage'])
