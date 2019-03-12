# IcsToGnomeCalendar
IcsToGnomeCalendar is a simple utility to add ICS file to GnomeCalendar. 

# Why?
It's actually pretty useful if you find Evolution or Thunderbird too ugly to use some other email client (i.e. Mailspring) which hasn't got calendar integration or just prefer Gnome Calendar over other external tools

# Installation
It's pretty complicated for now but I'm going to simplify it soon:
  * Install python3 and pyyaml:
        
        # Debian-derivatives only command
        sudo apt-get update && sudo apt-get install python3 python3-pip && sudo pip3 install pyyaml

  * Create empty calendar file template, for example `~/calendar.ics` with content:
    
    
        BEGIN:VCALENDAR
        PRODID:-//Microsoft Corporation//Outlook 15.0 MIMEDIR//EN
        VERSION:2.0
        METHOD:REQUEST
        X-MS-OLK-FORCEINSPECTOROPEN:TRUE
        X-EVOLUTION-DATA-REVISION:2019-03-12T14:28:54.735649Z(42)
        BEGIN:VTIMEZONE
        TZID:Central European Standard Time
        BEGIN:STANDARD
        DTSTART:16011028T030000
        RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=10
        TZOFFSETFROM:+0200
        TZOFFSETTO:+0100
        END:STANDARD
        BEGIN:DAYLIGHT
        DTSTART:16010325T020000
        RRULE:FREQ=YEARLY;BYDAY=-1SU;BYMONTH=3
        TZOFFSETFROM:+0100
        TZOFFSETTO:+0200
        END:DAYLIGHT
        END:VTIMEZONE
        END:VCALENDAR

  
  * Import `calendar.ics` to Gnome Calendar
    1. Open Gnome Calendar
    2. calendar settings
    3. Add
    4. From file
    5. Select calendar.ics
    
  * Find out our calendar identifier. The best (and the only) way I know is to:
    1. Close calendar
    
            gnome-calendar -q
    
    2. Open calendar in debug mode in terminal:
    
            gnome-calendar --debug
        
    3. Find line similar to the following and save SomeRandomCode somewhere
    
            15:45:20.0714               GcalManager:    DEBUG: Source YourCalendarName (SomeRandomCode) connected
            
    4. Create file `~/.ics_to_gnome` in your favourite text editor with content:
    
            calendarPath: <full_path_to_your_calendar>
            calendarUid: <somerandomcode_from_previous_step>
            
    5. Download `add-to-gnome-calendar.py` and copy it to `/usr/sbin/`:
            
            sudo cp <download_location>/add-to-gnome-calendar.py /usr/sbin/add-to-gnome-calendar && sudo chmod +x /usr/sbin/add-to-gnome-calendar
            
    6. Create file `~/.local/share/applications/AddToGnomeCalendar.desktop` with content:
    
            [Desktop Entry]
            Name=AddToGnomeCalendar
            Exec=add-to-gnome-calendar %u
            Icon=emacs-icon
            Type=Application
            Terminal=false
            NoDisplay=true
            MimeType=text/calendar;
            
    7. Open file `~/.config/mimeapps.list` and find lines starting with `text/calendar` and replace it with the following line (or add new ones under [Default Applications] and [Added Associations] if they don't exist):
    
            test/calendar=AddToGnomeCalendar.desktop
            
    8. Done! Any opened ics file should automatically add to your calendar! 
