
function draw_1(data) {
  var myChart = echarts.init(document.getElementById('draw_1'), 'customed');
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
      ['平均年龄', data[0][0], data[0][1]],
      ['平均飞行次数', data[1][0], data[1][1]],
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
