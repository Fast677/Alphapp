// src/community/backend/models/user.js
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const userSchema = new Schema({
    name: { type: String, required: true },
    email: { type: String, unique: true, required: true },
    hashedPassword: { type: String, required: true }, // **Importante: Almacenar contraseñas de forma segura**
    registrationDate: { type: Date, default: Date.now },
    role: { type: String, default: 'user' },
    // Otros campos relevantes:
    // - bio: Biografía del usuario
    // - profile_picture: Enlace a la imagen de perfil
});

module.exports = mongoose.model('User', userSchema);
