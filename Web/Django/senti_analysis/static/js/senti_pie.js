var myChart = echarts.init(document.getElementById("senti_pie"));
        //4.指定配置项和数据
        var option = {
              tooltip: {
                trigger: 'item'
              },
              legend: {
                top: '5%',
                left: 'center'
              },
              series: [
                {
                  name: 'Access From',
                  type: 'pie',
                  radius: ['40%', '70%'],
                  avoidLabelOverlap: false,
                  itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                  },
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
                  data: [
                    { value: 708, name: '正面' },
                    { value: 654, name: '中性' },
                    { value: 201, name: '负面' },

                  ]
                }
              ]
            };
        //5.将配置项设置给echarts实例对象，使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
//        window.addEventListener('resize', myChart.resize);