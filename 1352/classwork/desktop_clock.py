import datetime
import dudraw

def draw_clock(hour, minute, second):
    dudraw.set_font_family("Helvetica")
    dudraw.set_font_size(60)
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.text(0.5, 0.5, f'{str(hour)}:{str(minute)}:{str(second)}')

def main():

    dudraw.set_canvas_size(250, 100)
    while True:
        now = datetime.datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second
        
        if minute < 10:
            minute = f'0{minute}'
        if second < 10:
            second = f'0{second}'

        dudraw.clear(dudraw.LIGHT_GRAY)
        draw_clock(hour, minute, second)
        dudraw.show(100)
        
if __name__ == "__main__":
    main()