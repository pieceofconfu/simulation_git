import subprocess

subprocess.run("python big_ball.py", shell=True)







# # ana_program.py
# import rospy
# from big_ball import main as MoveObject
# # from medium_ball import main as medium_ball_main
# # from little_ball import main as little_ball_main
# # from big_ball_clone import main as big_ball_clone_main
# # from medium_ball_clone import main as medium_ball_clone_main
# # from big_ball_clone_clone import main as big_ball_clone_clone_main
# # from medium_ball_clone_0 import main as medium_ball_clone_0_main

# # Diğer ROS dosyalarını da buraya ekleyin

# if __name__ == '__main__':
#     rospy.init_node('ana_program', anonymous=True)

#     # Her bir ROS dosyasının sonsuz döngüsünü birleştirin
#     while not rospy.is_shutdown():
#         big_ball_instance = MoveObject()  # BigBall sınıfından bir örnek oluştur
#         big_ball_instance.run()  # ros_dosya1'deki sonsuz döngü
#         # medium_ball_main()  # ros_dosya2'deki sonsuz döngü
#         # little_ball_main()
#         # big_ball_clone_main()
#         # medium_ball_clone_main()
#         # big_ball_clone_clone_main()
#         # medium_ball_clone_0_main()
#         # # Diğer ROS dosyalarını da buraya ekleyin

