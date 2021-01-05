# `post/macos/zetant/trolling/say`

## Description

This module uses system `say` command to say message.

## Verification Steps

1. Start ZetaSploit
2. Run `exploit/macos/stager/zetant_reverse_tcp` on target
3. Do: `use post/macos/zetant/trolling/say`
4. Do: `set SESSION` to your target session
5. Do: `set MESSAGE` to your message
6. Do: `run`

## Options

| Option    | Default Value  | Required | Description        |
|-----------|----------------|----------|--------------------|
| `MESSAGE` | Hello, zetant! | yes      | Message to say.    |
| `SESSION` | 0              | yes      | Session to run on. |

**MESSAGE**

Variable that contains message you want device to say.

**SESSION**

Variable that contains session id to run post module on it.

## Scenarios

```
(zsf: post: macos/zetant/trolling/say)> run
[*] Sending message to device...
[+] Done saying message!
(zsf: post: macos/zetant/trolling/say)>
```
