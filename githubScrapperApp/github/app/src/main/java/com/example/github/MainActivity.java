package com.example.github;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.AbstractCollection;
import java.util.HashMap;
import java.util.Iterator;

public class MainActivity extends AppCompatActivity {
public static Object responce;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(this);
        if(sharedPreferences.getBoolean("login",false))
        {
            try {
                JSONObject json = new JSONObject(""+sharedPreferences.getString("response",""));
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }

        EditText username = findViewById(R.id.username);
        findViewById(R.id.submit).setOnClickListener(new View.OnClickListener() {
            private RequestQueue requestQueue;

            @Override
            public void onClick(View view) {
                String s = username.getText().toString();
                if(s.isEmpty()|| s==null){
                    Toast.makeText(MainActivity.this, "Enter Valid Username", Toast.LENGTH_SHORT).show();
                    return;
                }
                s = "https://adarshrawat7400.pythonanywhere.com/uname/"+s.trim();
                requestQueue = Volley.newRequestQueue(MainActivity.this);
                JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                        Request.Method.GET,
                        s,
                        null,
                        new Response.Listener() {
                            @Override
                            public void onResponse(Object response) {
                                responce = response;
                               SharedPreferences.Editor myEdit = sharedPreferences.edit();
                                myEdit.putBoolean("login", true);
                                myEdit.putString("response",""+response);
                                myEdit.apply();
                                Toast.makeText(MainActivity.this, ""+response , Toast.LENGTH_SHORT).show();
                                startActivity(new Intent(MainActivity.this,MainActivity2.class));
                            }

                           
                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error)
                            {
                                Toast.makeText(MainActivity.this, "Invalid UserName...", Toast.LENGTH_SHORT).show();
                            }
                        });
                requestQueue.add(jsonObjectRequest);
            }
        });
    }
}