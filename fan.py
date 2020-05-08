import time


def fan():
    while True:
        fo = open("/sys/class/thermal/thermal_zone0/temp", "r")
        # thermal_zone1是cpu的温度，thermal_zone2是gpu的温度，thermal_zone0的温度一直是最高的，可能
        # 是封装的温度，可用jtop查看具体的信息
        thermal = int(fo.read(10))
        fo.close()

        thermal = thermal / 1000
        #    print(thermal)
        if thermal < 30:
            thermal = 0
        elif thermal >= 30:
            thermal = thermal - 30

        thermal = str(int(thermal / 100 * 255))
        #    print(thermal)

        fw = open("/sys/devices/pwm-fan/target_pwm", "w")
        fw.write(thermal)
        fw.close()

        time.sleep(30)


if __name__ == "__main__":
    fan()
