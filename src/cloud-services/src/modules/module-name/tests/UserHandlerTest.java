// cloud-services/src/modules/module-name/tests/UserHandlerTest.java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import com.alphapp.modules.module_name.handlers.UserHandler;
import com.alphapp.modules.module_name.models.UserModel;
import com.alphapp.database.DatabaseService;

public class UserHandlerTest {

    private UserHandler userHandler;
    private DatabaseService databaseService;

    @BeforeEach
    void setUp() {
        // Inicializar mocks y el UserHandler antes de cada test
        databaseService = mock(DatabaseService.class);
        userHandler = new UserHandler(databaseService);
    }

    @Test
    void createUserTest() {
        // Datos de prueba para la creación de un usuario
        UserModel user = new UserModel();
        user.setName("Test User");
        user.setEmail("test@example.com");

        // Configurar el comportamiento esperado del mock de la base de datos
        when(databaseService.save(any(UserModel.class))).thenReturn(user);

        // Llamar al método a probar
        UserModel newUser = userHandler.createUser(user);

        // Verificar que el resultado es el esperado
        assertNotNull(newUser);
        assertEquals("Test User", newUser.getName());
        assertEquals("test@example.com", newUser.getEmail());

        // Verificar que el método save fue llamado en el servicio de base de datos
        verify(databaseService, times(1)).save(any(UserModel.class));
    }

    @Test
    void getUserByIdTest() {
        // ID de usuario para la prueba
        Long userId = 1L;

        // Configurar el comportamiento esperado del mock de la base de datos
        UserModel user = new UserModel();
        user.setId(userId);
        user.setName("Test User");
        user.setEmail("test@example.com");
        when(databaseService.getById(userId, UserModel.class)).thenReturn(user);

        // Llamar al método a probar
        UserModel retrievedUser = userHandler.getUserById(userId);

        // Verificar que el resultado es el esperado
        assertNotNull(retrievedUser);
        assertEquals(userId, retrievedUser.getId());
        assertEquals("Test User", retrievedUser.getName());
        assertEquals("test@example.com", retrievedUser.getEmail());

        // Verificar que el método getById fue llamado en el servicio de base de datos
        verify(databaseService, times(1)).getById(userId, UserModel.class);
    }

    @Test
    void updateUserTest() {
        // ID de usuario y datos actualizados para la prueba
        Long userId = 1L;
        UserModel updatedUser = new UserModel();
        updatedUser.setId(userId);
        updatedUser.setName("Updated User");
        updatedUser.setEmail("updated@example.com");

        // Configurar el comportamiento esperado del mock de la base de datos
        when(databaseService.update(any(UserModel.class))).thenReturn(updatedUser);

        // Llamar al método a probar
        UserModel result = userHandler.updateUser(updatedUser);

        // Verificar que el resultado es el esperado
        assertNotNull(result);
        assertEquals(userId, result.getId());
        assertEquals("Updated User", result.getName());
        assertEquals("updated@example.com", result.getEmail());

        // Verificar que el método update fue llamado en el servicio de base de datos
        verify(databaseService, times(1)).update(any(UserModel.class));
    }

    @Test
    void deleteUserTest() {
        // ID de usuario para la prueba
        Long userId = 1L;

        // Llamar al método a probar
        userHandler.deleteUser(userId);

        // Verificar que el método delete fue llamado en el servicio de base de datos
        verify(databaseService, times(1)).delete(userId, UserModel.class);
    }
}
