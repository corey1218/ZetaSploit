# `post/macos/zetant/gather/prompt`

## Description

This module uses system `osascript` to prompt user to type password.

## Verification Steps

1. Start ZetaSploit
2. Run `exploit/macos/stager/zetant_reverse_tcp` on target
3. Do: `use post/macos/zetant/gather/prompt`
4. Do: `set SESSION` to your target session
5. Do: `run`

## Options

| Option    | Default Value | Required | Description        |
|-----------|---------------|----------|--------------------|
| `SESSION` | 0             | yes      | Session to run on. |

**SESSION**

Variable that contains session id to run post module on it.

## Scenarios

```
(zsf: post: macos/zetant/gather/prompt)> run
[*] Waiting for prompt window to appear...
[*] Waiting for user to type password...
[i] User entered: mysuperstrongpassword1234
(zsf: post: macos/zetant/gather/prompt)>
```
