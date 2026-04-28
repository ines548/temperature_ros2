cmake_minimum_required(VERSION 3.5)
project(my_first_package)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Génération du service
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Calcul.srv"
)

# Installer le package Python
ament_python_install_package(${PROJECT_NAME})

install(
  PROGRAMS
    my_first_package/calcule_service.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
