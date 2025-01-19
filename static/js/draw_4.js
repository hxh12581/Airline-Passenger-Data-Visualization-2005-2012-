// myEchartConfig.js
function draw_4(data) {
  var myChart = echarts.init(document.getElementById('draw_4'), 'customed');
  var option = {
  legend: {
    textStyle: {
      color: 'white'  // 设置图例文字颜色为白色
    }
  },
  tooltip: {},
  dataset: {
    source: [
      ['product','女','男'],
      ['平均乘机时间间隔', data[0][0], data[0][1]],
      ['平均总飞行公里数', data[1][0], data[1][1]],
    ]
  },
  xAxis: {
    type: 'category',
    axisLabel: {
      color: 'white' // 设置 x 轴上的文字颜色为白色
    }
  },
  yAxis: {
    axisLabel: {
      color: 'white' // 设置 y 轴上的文字颜色为白色
    }

  },
  series: [{ type: 'bar' }, { type: 'bar' }]
};
  myChart.setOption(option);
}