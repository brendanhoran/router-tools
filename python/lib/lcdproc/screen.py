from .widgets import StringWidget, TitleWidget, HBarWidget, VBarWidget, IconWidget, ScrollerWidget, FrameWidget,NumberWidget


class Screen(object):

    """ LCDproc Screen Object """

    def __init__(self, server, ref):
        
        """ Constructor """
        
        self.server = server
        self.ref = ref
        self.name = ref
        self.width = None
        self.height = None
        self.priority = None
        self.heartbeat = None
        self.backlight = None
        self.duration = None
        self.timeout = None
        self.cursor = None
        self.cursor_x = None
        self.cursor_y = None
        self.widgets = dict()
        
        self.server.request("screen_add %s" % (ref))
        self.set_cursor("off")
        
        
    def set_name(self, name):
        
        """ Set Screen Name """
        
        self.name = name
        self.server.request("screen_set %s name %s" % (self.ref, self.name))


    def set_width(self, width):
        
        """ Set Screen Width """
        
        if width > 0 and width <= self.server.server_info.get("screen_width"):
            self.width = width
            self.server.request("screen_set %s wid %i" % (self.ref, self.width))


    def set_height(self, height):

        """ Set Screen Height """
        
        if height > 0 and height <= self.server.server_info.get("screen_height"):
            self.height = height
            self.server.request("screen_set %s hgt %i" % (self.ref, self.height))


    def set_cursor_x(self, x):

        """ Set Screen Cursor X Position """
        
        if x >= 0 and x <= self.server.server_info.get("screen_width"):
            self.cursor_x = x
            self.server.request("screen_set %s cursor_x %i" % (self.ref, self.cursor_x))


    def set_cursor_y(self, y):

        """ Set Screen Cursor Y Position """
        
        if y >= 0 and y <= self.server.server_info.get("screen_height"):
            self.cursor_y = y
            self.server.request("screen_set %s cursor_y %i" % (self.ref, self.cursor_y))


    def set_duration(self, duration):

        """ Set Screen Change Interval Duration """
        
        if duration > 0:
            self.duration = duration
            self.server.request("screen_set %s duration %i" % (self.ref, (self.duration * 8)))


    def set_timeout(self, timeout):

        """ Set Screen Timeout Duration """
        
        if timeout > 0:
            self.timeout = timeout
            self.server.request("screen_set %s timeout %i" % (self.ref, (self.timeout * 8)))


    def set_priority(self, priority):
    
        """ Set Screen Priority Class """
        
        if priority in ["hidden", "background", "info", "foreground", "alert", "input"]:
            self.priority = priority
            self.server.request("screen_set %s priority %s" % (self.ref, self.priority))
        
        
    def set_backlight(self, state):
        
        """ Set Screen Backlight Mode """
        
        if state in ["on", "off", "toggle", "open", "blink", "flash"]:
            self.backlight = state
            self.server.request("screen_set %s backlight %s" % (self.ref, self.backlight))


    def set_heartbeat(self, state):

        """ Set Screen Heartbeat Display Mode """
        
        if state in ["on", "off", "open"]:
            self.heartbeat = state
            self.server.request("screen_set %s heartbeat %s" % (self.ref, self.heartbeat))


    def set_cursor(self, cursor):
        
        """ Set Screen Cursor Mode """
        
        if cursor in ["on", "off", "under", "block"]:
            self.cursor = cursor
            self.server.request("screen_set %s cursor %s" % (self.ref, self.cursor))

            
    def clear(self):
        
        """ Clear Screen """
        
        w1 = StringWidget(self, ref="_w1_", text=" "*20, x=1, y=1)
        w2 = StringWidget(self, ref="_w2_", text=" "*20, x=1, y=2)
        w3 = StringWidget(self, ref="_w3_", text=" "*20, x=1, y=3)
        w4 = StringWidget(self, ref="_w4_", text=" "*20, x=1, y=4)
            

    def add_string_widget(self, ref, text="Text", x=1, y=1):     
    
        """ Add String Widget """
        
        if ref not in self.widgets:   
            widget = StringWidget(screen=self, ref=ref, text=text, x=x, y=y)
            self.widgets[ref] = widget
            return self.widgets[ref]


    def add_title_widget(self, ref, text="Title"):     

        """ Add Title Widget """
        
        if ref not in self.widgets:   
            widget = TitleWidget(screen=self, ref=ref, text=text)
            self.widgets[ref] = widget
            return self.widgets[ref]


    def add_hbar_widget(self, ref, x=1, y=1, length=10):     

        """ Add Horizontal Bar Widget """
        
        if ref not in self.widgets:   
            widget = HBarWidget(screen=self, ref=ref, x=x, y=y, length=length)
            self.widgets[ref] = widget
            return self.widgets[ref] 
            
            
    def add_vbar_widget(self, ref, x=1, y=1, length=10):     
        
        """ Add Vertical Bar Widget """
        
        if ref not in self.widgets:   
            widget = VBarWidget(screen=self, ref=ref, x=x, y=y, length=length)
            self.widgets[ref] = widget
            return self.widgets[ref]   
            
            
    def add_icon_widget(self, ref, x=1, y=1, name="heart"):     
        
        """ Add Icon Widget """
        
        if ref not in self.widgets:   
            widget = IconWidget(screen=self, ref=ref, x=x, y=y, name=name)
            self.widgets[ref] = widget
            return self.widgets[ref]   
            
            
    def add_scroller_widget(self, ref, left=1, top=1, right=20, bottom=1, direction="h", speed=1, text="Message"):     
        
        """ Add Scroller Widget """
        
        if ref not in self.widgets:   
            widget = ScrollerWidget(screen=self, ref=ref, left=left, top=top, right=right, bottom=bottom, direction=direction, speed=speed, text=text)
            self.widgets[ref] = widget
            return self.widgets[ref]    
        
        
    def add_frame_widget(self, ref, left=1, top=1, right=20, bottom=1, width=20, height=4, direction="h", speed=1):     
        
        """ Add Frame Widget """
        
        if ref not in self.widgets:   
            widget = FrameWidget(screen=self, ref=ref, left=left, top=top, right=right, bottom=bottom, width=width, height=height, direction=direction, speed=speed)
            self.widgets[ref] = widget
            return self.widgets[ref]        
        
        
    def add_number_widget(self, ref, x=1, value=1):     
        
        """ Add Number Widget """
        
        if ref not in self.widgets:   
            widget = NumberWidget(screen=self, ref=ref, x=x, value=value)
            self.widgets[ref] = widget
            return self.widgets[ref]
        
                                            

    def del_widget(self, ref):
        """ Delete/Remove A Widget """
        self.server.request("widget_del %s %s" % (self.name, ref))
        del(self.widgets[ref])
