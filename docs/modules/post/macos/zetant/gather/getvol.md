# `post/macos/zetant/gather/getvol`

## Vulnerable Application

This module uses system `osascript` to dump system volume level.

## Verification Steps

  1. Start ZetaSploit
  2. Run `exploit/macos/stager/zetant_reverse_tcp` on target.
  3. Do: `use post/macos/zetant/gather/getvol`
  4. Do: `set SESSION` to your target session
  5. Do: `run`
  6. You should see volume level

## Options

| Option    | Default Value | Required | Description        |
|-----------|---------------|----------|--------------------|
| `SESSION` | 0             | True     | Session to run on. |

## Scenarios

```
(zsf: post: macos/zetant/gather/getvol)> run

[i] Volume Level: 25
```
