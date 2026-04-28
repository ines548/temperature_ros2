#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from calcule_srv.srv import Calcule

class CalculeServer(Node):
    def __init__(self):
        super().__init__('calcule_server')
        self.srv = self.create_service(Calcule, 'calcule', self.calcule_callback)
        self.get_logger().info('Serveur /calcule prêt.')

    def calcule_callback(self, request, response):
        a, b, op = request.a, request.b, request.op.strip()
        self.get_logger().info(f'Requête : {a} {op} {b}')
        if op == '+':
            response.result = a + b
        elif op == '-':
            response.result = a - b
        elif op == '*':
            response.result = a * b
        elif op == '/':
            response.result = a / b if b != 0.0 else float('nan')
        else:
            response.result = float('nan')
        self.get_logger().info(f'Résultat : {response.result}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CalculeServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
