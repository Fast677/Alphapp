const express = require('express');
const router = express.Router();
const userController = require('../controllers/user_controller'); // Ajusta la ruta según tu proyecto

router.get('/users', userController.userList);
router.get('/users/:id', userController.userDetail);
router.post('/users', userController.userCreate);
router.put('/users/:id', userController.userUpdate);
router.delete('/users/:id', userController.userDelete);

module.exports = router;
