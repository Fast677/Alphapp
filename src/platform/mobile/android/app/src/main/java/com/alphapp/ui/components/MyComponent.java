package com.alphapp.ui.components;

import android.content.Context;
import android.util.AttributeSet;
import android.view.LayoutInflater;
import android.widget.LinearLayout;
import android.widget.TextView;
import com.alphapp.R;

public class MyComponent extends LinearLayout {

    private TextView myTextView;

    public MyComponent(Context context) {
        super(context);
        init(context);
    }

    public MyComponent(Context context, AttributeSet attrs) {
        super(context, attrs);
        init(context);
    }

    public MyComponent(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        init(context);
    }

    private void init(Context context) {
        LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        inflater.inflate(R.layout.my_component, this, true);

        myTextView = findViewById(R.id.my_text_view);
    }

    public void setText(String text) {
        myTextView.setText(text);
    }
}
