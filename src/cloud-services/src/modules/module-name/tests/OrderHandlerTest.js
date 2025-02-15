// cloud-services/src/modules/module-name/tests/OrderHandlerTest.js
const OrderHandler = require('../handlers/OrderHandler');
const OrderModel = require('../models/OrderModel');
const Database = require('../../utils/Database');

describe('OrderHandler', () => {
    let orderHandler;
    let database;

    beforeAll(() => {
        database = new Database();
    });

    beforeEach(() => {
        orderHandler = new OrderHandler(database);
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    afterAll(() => {
        database.close();
    });

    it('should create a new order', async () => {
        const orderData = {
            userId: 1,
            items: [{ productId: 101, quantity: 2 }],
            totalAmount: 100,
        };

        jest.spyOn(database, 'save').mockImplementation(async (order) => {
            order.id = 1;
            return order;
        });

        const newOrder = await orderHandler.createOrder(orderData);

        expect(newOrder).toBeInstanceOf(OrderModel);
        expect(newOrder.id).toBe(1);
        expect(newOrder.userId).toBe(orderData.userId);
        expect(database.save).toHaveBeenCalled();
    });

    it('should get an order by id', async () => {
        const orderId = 1;
        const mockOrder = new OrderModel({
            id: orderId,
            userId: 1,
            items: [{ productId: 101, quantity: 2 }],
            totalAmount: 100,
        });

        jest.spyOn(database, 'getById').mockResolvedValue(mockOrder);

        const order = await orderHandler.getOrderById(orderId);

        expect(order).toBeInstanceOf(OrderModel);
        expect(order.id).toBe(orderId);
        expect(database.getById).toHaveBeenCalledWith('orders', orderId);
    });

    it('should cancel an order', async () => {
        const orderId = 1;
        const mockOrder = new OrderModel({
            id: orderId,
            userId: 1,
            items: [{ productId: 101, quantity: 2 }],
            totalAmount: 100,
            status: 'pending',
        });

        jest.spyOn(database, 'getById').mockResolvedValue(mockOrder);
        jest.spyOn(database, 'update').mockResolvedValue({ ...mockOrder, status: 'cancelled' });

        const cancelledOrder = await orderHandler.cancelOrder(orderId);

        expect(cancelledOrder.status).toBe('cancelled');
        expect(database.getById).toHaveBeenCalledWith('orders', orderId);
        expect(database.update).toHaveBeenCalledWith('orders', orderId, { status: 'cancelled' });
    });
});
