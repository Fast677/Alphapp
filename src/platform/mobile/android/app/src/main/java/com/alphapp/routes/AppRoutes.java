package com.alphapp.routes;

import android.content.Context;
import android.content.Intent;

import com.alphapp.ui.pages.HomePage;
import com.alphapp.ui.pages.LoginPage;
import com.alphapp.ui.pages.ProfilePage;

public class AppRoutes {

    private Context context;

    public AppRoutes(Context context) {
        this.context = context;
    }

    public void navigateToHome() {
        Intent intent = new Intent(context, HomePage.class);
        context.startActivity(intent);
    }

    public void navigateToLogin() {
        Intent intent = new Intent(context, LoginPage.class);
        context.startActivity(intent);
    }

    public void navigateToProfile() {
        Intent intent = new Intent(context, ProfilePage.class);
        context.startActivity(intent);
    }
}
