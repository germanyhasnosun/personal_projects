function test_selections(sel){

    var selected_diagram = sel.options[sel.selectedIndex].value;

    if (selected_diagram == 'age'){
        document.getElementById('age_input_label').style.display = 'block';
        document.getElementById('age_input').style.display = 'block';
    }else{
        document.getElementById('age_input_label').style.display = 'none';
        document.getElementById('age_input').style.display = 'None';
    }


    if (selected_diagram == 'gender'){
        document.getElementById('gender_selection').style.display = 'block';
    }else{
        document.getElementById('gender_selection').style.display = 'None';
    }

    if (selected_diagram == 'location'){
        document.getElementById('location_selection').style.display = 'block';
    }else{
        document.getElementById('location_selection').style.display = 'None';
    }


}