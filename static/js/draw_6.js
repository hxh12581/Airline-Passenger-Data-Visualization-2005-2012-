function draw_6(data) {
  var myChart = echarts.init(document.getElementById('draw_6'), 'customed');
  var pieData = [];
  for (var i = 0; i < 4; i++) {
    pieData.push({
      value: data[1][i],
      name: data[0][i],
    });
  }
  var option = {
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',  // 设置图例布局为垂直方向
      top: 'middle',       // 通过调整 top 属性垂直居中图例
      left: 'left',        // 控制图例在左侧的位置
      right: 'right',      // 控制图例在右侧的位置
      textStyle: {
        color: 'white'  // 设置图例字体颜色为白色
      }
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 40,
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: pieData
      }
    ]
  };
  myChart.setOption(option);
}