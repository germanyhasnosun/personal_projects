
function chart_controller(){

    clear_canvas();

    var diagram_selected = document.getElementById('diagram_selection');
    
    var required_chart = diagram_selected.options[diagram_selected.selectedIndex].value;

    if (required_chart == 'age'){
          var chart_data_url = '/get_data/age';
          var selected_value= document.getElementById('age_input').value;
    }else if (required_chart == 'gender'){
          var chart_data_url = '/get_data/gender';
          var gender_select = document.getElementById('gender_selection');
          var selected_value= gender_select.options[gender_select.selectedIndex].text;
    }else if (required_chart == 'location'){
          var chart_data_url = '/get_data/location';
          var location_selection = document.getElementById('location_selection');
          var selected_value= location_selection.options[location_selection.selectedIndex].text;
}

    get_graph_data(chart_data_url,required_chart, selected_value);



  }

function get_graph_data(chart_data_url, required_chart,selected_value){

    var url = chart_data_url;


    $.ajax({
      url: "https://check-this-out.link" + url,
      type: 'GET',
      contentType: "application/json; charset=utf-8",
      dataType: 'json', // added data type
      success: function(data) {

          build_chart_params(data,required_chart,selected_value)
      }
  });




  }

function build_chart_params(graph_data,required_chart, selected_value){

  if (required_chart == 'age'){
    var user_selection = Math.round(selected_value/5,0)*5;

    var graph_labels = {
      dataset_label:'Risk group given age in percentage (%)',
      y_axis_label: 'Relative risk given patients age in Percent (%)',
      x_axis_label: 'Age of patient',
    }

  }else if (required_chart == 'gender'){
    var user_selection =selected_value;
    var graph_labels = {
      dataset_label:'Risk group given gender in percentage (%)',
      y_axis_label: 'Relative risk given patients gender in Percent (%)',
      x_axis_label: 'Gender',
    }
  }else{
    var user_selection =selected_value;
    var graph_labels = {
      dataset_label:'Risk group given location of mole in percentage (%)',
      y_axis_label: 'Relative risk given location of mole in Percent (%)',
      x_axis_label: 'Location of mole',
    }
  }


  var background_color_arrary = []
  var border_color_arrary = []
  
  for (var i = 0; i < graph_data.labels.length; i++){
    if (graph_data.labels[i] == user_selection){
      background_color_arrary.push('rgba(255, 99, 132, 0.2)')
      border_color_arrary.push('rgb(255, 99, 132)')
    }else{
      background_color_arrary.push('rgba(201, 203, 207, 0.2)')
      border_color_arrary.push('rgb(201, 203, 207)')
    }
  }
  


  var graph_arrary = {
    graph_background_color_arrary:background_color_arrary,
    graph_border_color_arrary:border_color_arrary,
    graph_labels:graph_labels,
    graph_data:graph_data,
  }

  build_final_chart(graph_arrary);

}


function build_final_chart(graph_arrary){


const data = {
  
  labels: graph_arrary.graph_data.labels,
  datasets: [{
    label: graph_arrary.graph_labels.dataset_label,
    data: graph_arrary.graph_data.values,
    backgroundColor: graph_arrary.graph_background_color_arrary,
    borderColor: graph_arrary.graph_border_color_arrary ,
    borderWidth: 1
  }]
};

console.log(data);


const config = {
  type: 'bar',
  data: data,
  options: {
    scales: {
      y: {
        beginAtZero: true
      },
      yAxes: [
        {
        scaleLabel: {
          display: true,
          labelString: graph_arrary.graph_labels.y_axis_label
        }
      }],
      xAxes: [
        {
        scaleLabel: {
          display: true,
          labelString: graph_arrary.graph_labels.x_axis_label
        }
      }    
    ]
    },
  },
};


new Chart(document.getElementById('myChart'),config);

}



function clear_canvas(){

  document.getElementById('myChart').remove();
  document.getElementById("histogram_chart").innerHTML = '<canvas id="myChart"></canvas>';

}