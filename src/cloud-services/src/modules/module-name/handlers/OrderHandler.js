// cloud-services/src/modules/module-name/handlers/OrderHandler.js

/**
 * Este módulo maneja las operaciones relacionadas con las órdenes.
 */
class OrderHandler {
  constructor(orderService) {
    this.orderService = orderService;
  }

  /**
   * Crea una nueva orden.
   * @param {Object} req - Objeto de solicitud HTTP.
   * @param {Object} res - Objeto de respuesta HTTP.
   */
  async createOrder(req, res) {
    try {
      const orderData = req.body;
      const newOrder = await this.orderService.createOrder(orderData);
      res.status(201).json(newOrder);
    } catch (error) {
      console.error("Error al crear la orden:", error);
      res.status(500).json({ error: "No se pudo crear la orden" });
    }
  }

  /**
   * Obtiene una orden por su ID.
   * @param {Object} req - Objeto de solicitud HTTP.
   * @param {Object} res - Objeto de respuesta HTTP.
   */
  async getOrder(req, res) {
    try {
      const orderId = req.params.id;
      const order = await this.orderService.getOrder(orderId);
      if (order) {
        res.status(200).json(order);
      } else {
        res.status(404).json({ message: "Orden no encontrada" });
      }
    } catch (error) {
      console.error("Error al obtener la orden:", error);
      res.status(500).json({ error: "No se pudo obtener la orden" });
    }
  }

  /**
   * Actualiza una orden existente.
   * @param {Object} req - Objeto de solicitud HTTP.
   * @param {Object} res - Objeto de respuesta HTTP.
   */
  async updateOrder(req, res) {
    try {
      const orderId = req.params.id;
      const orderData = req.body;
      const updatedOrder = await this.orderService.updateOrder(orderId, orderData);
      if (updatedOrder) {
        res.status(200).json(updatedOrder);
      } else {
        res.status(404).json({ message: "Orden no encontrada" });
      }
    } catch (error) {
      console.error("Error al actualizar la orden:", error);
      res.status(500).json({ error: "No se pudo actualizar la orden" });
    }
  }

  /**
   * Elimina una orden por su ID.
   * @param {Object} req - Objeto de solicitud HTTP.
   * @param {Object} res - Objeto de respuesta HTTP.
   */
  async deleteOrder(req, res) {
    try {
      const orderId = req.params.id;
      const result = await this.orderService.deleteOrder(orderId);
      if (result) {
        res.status(204).send();
      } else {
        res.status(404).json({ message: "Orden no encontrada" });
      }
    } catch (error) {
      console.error("Error al eliminar la orden:", error);
      res.status(500).json({ error: "No se pudo eliminar la orden" });
    }
  }
}

module.exports = OrderHandler;
