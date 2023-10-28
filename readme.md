A small utility to automate desktop applications. The received .exe should be dragged in to a Windows Terminal window; and pass 'steps' text file as argument; and hit enter. Possible steps are FOCUS, SENDKEY, WAIT, and GETURL.

FOCUS: Will take .exe app path; run it, if not already running; and bring it to the foreground.

SENDKEY: Any key on keyboard; and any number of key combination to be sent to the active GUI. Following are the valid key names:

Esc, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Print Screen, Pause, Insert, Del, Home, ~, `, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, !, @, #, $, %, ^, &, *, (, ), -, _, Plus, =, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, [, ], {, }, \, |, :, ;, ", ', <, >, ., ,, ?, /, Left, Right, Up, Down, PageUp, PageDn, Windows, Menu, Fn, Space, Enter, Backspace, LShift, RShift, LCtrl, RCtrl, LAlt, RAlt, Tab, Caps Lock, Num Lock

WAIT: Being idle for x (user defined) seconds.

TERMINATE: Terminate all processes of defined .exe.

TYPETEXT: Type any given text literally, with optional key press delay in seconds.

GETURL: Send a http pr https request; it will return nothing.

Steps must be defined in 'steps.txt' file, which must be present in the root directory of the executable. Example 'steps.txt' text file:

FOCUS "C:\Program Files\Kaslaan DocConvert\Kaslaan DocConvert.exe"
WAIT 5
TYPETEXT "Mango" 0.3
SENDKEY LAlt+F4
GETURL "https://google.com"
