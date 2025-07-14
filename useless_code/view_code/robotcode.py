from fanucpy import Robot
import numpy as np

if __name__ == "__main__":
    robot = Robot(
        robot_model="Fanuc",
        host="129.129.178.127",
        port=18735,
        ee_DO_type="RDO",
        ee_DO_num=7,
    )

    try:
        test = robot.connect()
        print(test)
    except:
        print("didnt work")

    # get robot state
    print("Current poses: ")
    cur_pos = robot.get_curpos()
    cur_jpos = robot.get_curjpos()
    print(f"Current pose: {cur_pos}")
    print(f"Current joints: {cur_jpos}")

    # move in cartesian space
    robot.move(
        "pose",
        vals=np.array(cur_pos) + 0.5,
        velocity=50,
        acceleration=50,
        cnt_val=0,
        linear=False,
    )

    print("Poses after moving: ")
    cur_pos = robot.get_curpos()
    cur_jpos = robot.get_curjpos()
    print(f"Current pose: {cur_pos}")
    print(f"Current joints: {cur_jpos}")

    # robot.move(
    #     "pose",
    #     vals=[153.31,331.91,np.array(cur_pos)[2],np.array(cur_pos)[3],np.array(cur_pos)[4],np.array(cur_pos)[5]],
    #     velocity=50,
    #     acceleration=50,
    #     cnt_val=0,
    #     linear=False,
    #     )

    # print("Poses after moving: ")
    # cur_pos = robot.get_curpos()
    # cur_jpos = robot.get_curjpos()
    # print(f"Current pose: {cur_pos}")
    # print(f"Current joints: {cur_jpos}")

    print("get/set DOUT")
    print(robot.get_dout(123))
    robot.set_dout(123, True)
    print(robot.get_dout(123))