CoordMode, Pixel, Screen  
CoordMode, Mouse, Screen 

resolution := A_Args[1]
litemode := A_Args[2]

FindLiteButton()
{
    
    global resolution  
    
    Loop
    {
        if (resolution = "1440p")
        {
            PixelSearch, FoundX, FoundY, 75, 1213, 475, 1288, 0xFF557F, 0, Fast RGB
        }
        else if (resolution == "1080p")
        {
            PixelSearch, FoundX, FoundY, 57, 913, 355, 969, 0xFF557F, 0, Fast RGB
        }
        else
            MsgBox, Invalid resolution
        
        ; Check if the color was found
        if ErrorLevel = 0
        {
            WinActivate, Roblox
            WinWaitActive, Roblox
            WinMaximize, Roblox
            MouseMove, FoundX, FoundY
            Sleep, 80
            MouseClick, left
            FindPlayButton()
            break
        }
        Sleep, 10
    }
}

FindPlayButton()
{
    global resolution
    
    Loop
    {
        if (resolution == "1440p")
            PixelSearch, FoundX, FoundY, 42, 211, 506, 300, 0xAAFF7F, 0, Fast RGB
        else if (resolution == "1080p")
            PixelSearch, FoundX, FoundY, 34, 170, 380, 235, 0xAAFF7F, 0, Fast RGB
        else
            MsgBox, Invalid resolution

        ; Check if the color was found
        if ErrorLevel = 0
        {
            WinActivate, Roblox
            WinWaitActive, Roblox
            WinMaximize, Roblox
            MouseMove, FoundX, FoundY
            Sleep, 150
            MouseClick, left
            sleep, 1000
            GetThermos()
            break
        }

        Sleep, 10
    }
}

GetThermos()
{
    global resolution
    
    color_stable_time := 1000 ; 1000 milliseconds (1 second)
    color_stable := false
    stable_start := 0

    Loop
    {
        if (resolution == "1440p")
            PixelSearch, FoundX, FoundY, 1275, 73, 1289, 61, 0x323232, 0, RGB
        else if (resolution == "1080p")
            PixelSearch, FoundX, FoundY, 960, 73, 974, 61, 0x323232, 0, RGB
        else
            MsgBox, Invalid resolution

        if ErrorLevel = 0
        {
            if (color_stable && A_TickCount - stable_start >= color_stable_time)
            {
                WinActivate, Roblox
                WinWaitActive, Roblox
                WinMaximize, Roblox
                
                MouseMove, FoundX, FoundY
                Sleep, 150
                MouseClick, left
                break
            }
            else if (!color_stable)
            {
                ; Start the timer if the color becomes stable
                color_stable := true
                stable_start := A_TickCount
            }
        }
        else
        {
            color_stable := false
        }

        Sleep, 10
    }

    Loop
    {
        if (resolution == "1440p")
            PixelSearch, FoundX, FoundY, 1205, 98, 1226, 71, 0x323232, 0, RGB

        else if (resolution == "1080p")
			PixelSearch, FoundX, FoundY, 885, 60, 908, 98, 0x323232, 0, RGB
		else
			MsgBox, Invalid resolution
        ; Check if the color was found
        if ErrorLevel = 0
        {
            WinActivate, Roblox
            WinWaitActive, Roblox
            WinMaximize, Roblox
            
            MouseMove, FoundX, FoundY
            Sleep, 150
            MouseClick, left
            break
        }
    }
}

if (litemode == "True")
{
	FindLiteButton()
}
else if (litemode == "False")
{
	FindPlayButton()
}
else
{
	MsgBox, Invalid Option For LiteMode
}