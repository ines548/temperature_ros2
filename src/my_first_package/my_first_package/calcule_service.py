import rclpy
from rclpy.node import Node
from my_first_package.srv import Calcul  # le service que tu as créé

class CalculeService(Node):
    def __init__(self):
        super().__init__('calcule_service')
        self.srv = self.create_service(Calcul, 'calcule', self.calcule_callback)
        self.get_logger().info('Service /calcule prêt')

    def calcule_callback(self, request, response):
        a = request.a
        b = request.b
        op = request.op

        try:
            if op == '+':
                response.result = a + b
            elif op == '-':
                response.result = a - b
            elif op == '*':
                response.result = a * b
            elif op == '/':
                response.result = a / b
            else:
                self.get_logger().warn(f'Opération inconnue: {op}')
                response.result = 0.0
        except Exception as e:
            self.get_logger().error(f'Erreur: {e}')
            response.result = 0.0

        return response

def main(args=None):
    rclpy.init(args=args)
    node = CalculeService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
