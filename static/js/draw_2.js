// myEchartConfig.js
function draw_2(data) {
  var myChart = echarts.init(document.getElementById('draw_2'), 'customed');
  var option = {
    tooltip: {},
    legend: {
      textStyle: {
        color: 'white'
      },
      data: ['活跃时长']
    },
    xAxis: {
      type: 'category',
      axisLine: {
        lineStyle: {
          color: 'white'
        }
      },
      axisLabel: {
        color: 'white',
        textStyle: {
           fontSize: 6
    }
      },
      nameTextStyle: {
        color: 'white'
      },
      data: data[0],
    },
    yAxis: {
      axisLine: {
        lineStyle: {
          color: 'white'
        }
      },
       axisLabel: {
      color: 'white' // 设置 y 轴上的文字颜色为白色
    }
    },
    series: [
      {
        name: '活跃时长',
        type: 'bar',
        data: data[1]
      },
    ]
  };

  myChart.setOption(option);
}