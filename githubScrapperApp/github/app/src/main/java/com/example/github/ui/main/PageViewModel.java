package com.example.github.ui.main;

import android.util.Log;
import android.widget.Toast;

import androidx.arch.core.util.Function;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.Transformations;
import androidx.lifecycle.ViewModel;

import com.example.github.MainActivity;

import org.json.JSONObject;

import java.io.CharArrayWriter;

public class PageViewModel extends ViewModel {

    private MutableLiveData<Integer> mIndex = new MutableLiveData<>();
    private LiveData<String> mText = Transformations.map(mIndex, new Function<Integer, String>() {
        @Override
        public String apply(Integer input) {
            try {
                String s = "" + ((JSONObject) MainActivity.responce).getJSONObject("UserInformation");
                s+="\n";
                s = s.replace("{","");
                s = s.replace("}","");
                s = s.replace("\"","");
                s = s.replace(":"," : ");
                s = s.replace(",","\n");
                s = s.replace("\\","");
                s+="\n";
                String s1 = "" + ((JSONObject) MainActivity.responce).getJSONArray("Repositories");
                s1 = s1.replace("[","");
                s1 = s1.replace("]","");
                s1 = s1.replace("{","");
                s1 = s1.replace("}","");
                s1 = s1.replace("\"","");
                s1 = s1.replace(":"," : ");
                s1 = s1.replace(",","\n");
                s1 = s1.replace("\\","");
                s1 = s1.replace("Name","\nName");
                s1+="\n";
                String s2 = "" + ((JSONObject) MainActivity.responce).getJSONArray("ContributionForOrganistions");
                s2 = s2.replace("[","");
                s2 = s2.replace("]","");
                s2 = s2.replace("{","");
                s2 = s2.replace("}","");
                s2 = s2.replace("\"","");
                s2 = s2.replace(":"," : ");
                s2 = s2.replace(",","\n");
                s2 = s2.replace("\\","");
                s2+="\n";



                switch (input) {
                    case 1:
                        return s;
                        case 2:
                            return s1;
                    case 3:
                        return s2;
                }
            }catch (Exception e){
                Log.d("kasjkdjksa",""+e);
            }
            return "Hello world from section: " + input;
        }
    });

    public void setIndex(int index) {
        mIndex.setValue(index);
    }

    public LiveData<String> getText() {
        return mText;
    }
}