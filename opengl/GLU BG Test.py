import glfw
from OpenGL.GL import *

def main():

    # initialize glfw
    if not glfw.init():
        return

    window = glfw.create_window(200,200,"Testing Windows", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glClearColor(0.2, 0.5, 0.2, 1.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()