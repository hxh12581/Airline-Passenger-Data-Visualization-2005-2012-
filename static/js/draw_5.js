// myEchartConfig.js
function draw_5(data) {
  var myChart = echarts.init(document.getElementById('draw_5'), 'customed');
  var option = {
    tooltip: {},
    legend: {
      textStyle: {
        color: 'white'
      },
      data: ['平均折扣率']
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
      }, axisLabel: {
      color: 'white' // 设置 y 轴上的文字颜色为白色
    }
    },
    series: [
      {
        name: '平均折扣率',
        type: 'line',
        data: data[1]
      },
    ]
  };

  myChart.setOption(option);
}