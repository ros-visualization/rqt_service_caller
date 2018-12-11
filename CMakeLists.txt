cmake_minimum_required(VERSION 3.5)
project(rqt_service_caller)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rqt_py_common REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(srv_files
  "srv/Sum.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${srv_files}
  DEPENDENCIES rqt_py_common
  ADD_LINTER_TESTS
)

ament_python_install_package(${PROJECT_NAME}
  PACKAGE_DIR src/${PROJECT_NAME})

install(FILES plugin.xml
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY resource
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS scripts/example_service
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS scripts/rqt_service_caller
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rqt_py_common)
ament_export_dependencies(rosidl_default_runtime)

ament_package()
