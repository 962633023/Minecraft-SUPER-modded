"""
Hello!
Welcome to the Minecraft Map creator.
In this file, you can design maps for gamemodes!!!
"""

game = []
for i in range(2601):
    game += [' ']
place = 2503
game[2503] = '🙂'
game[2551:2558] = '∥', '∥', '∥', '∥', '∥', '∥', '∥'
game[2296], game[2302], game[2347], game[2353], game[2398], game[2404], game[2449], game[2455], game[2500] = \
    '|', '|', '|', '|', '|', '|', '|', '|', '|'
game[2558:2565] = '▪', '▪', '▪', '▪', '▪', '▪', '▪'
game[2245:2252] = game[2551:2558]
game[2501:2503] = '◈', '◈'
game[2504] = '⊠'
game[2509:2512] = '◆', '◆', '◆'
game[2459] = '◆'
game[2456] = '◆'
game[2354] = '◆'
game[2196:2200] = '⌘', '⌘', '⌘', '⌘', '⌘'
game[2146:2149] = '⌘', '⌘', '⌘'
game[2096] = '⌘'
game[2592:2599] = game[2552:2559]
game[2585:2592] = game[2559:2566]
game[2286:2293] = game[2246:2253]
game[2236:2241] = game[2196:2201]
game[2186:2189] = game[2146:2149]
game[2136] = '⌘'
game[2337], game[2343], game[2388], game[2394], game[2439], game[2445], game[2490], game[2496], game[2547] = \
    '|', '|', '|', '|', '|', '|', '|', '|', '|'
game[2545:2547] = '◈', '◈'
game[2544] = '☹️'
game[2536:2539] = game[2510:2513]
game[2543] = '⊠'
game[2486] = '◆'
game[2489] = '◆'
game[2387] = '◆'
k = 0
while k < 51:
    print(game[k * 51: (k + 1) * 51])
    k += 1
