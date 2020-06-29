var layer = 0; //图层索引  
CanvasExt = {
    drawPen: function (canvasId, penColor) {
        var that = this;
        that.penColor = penColor;
        // that.penWidth = penWidth;
        //canvas DOM对象  
        var canvas = document.getElementById(canvasId);
        //canvas 的矩形框
        var canvasRect = canvas.getBoundingClientRect();

        //矩形框的左上角坐标
        var canvasLeft = canvasRect.left;
        var canvasTop = canvasRect.top;

        //画图坐标原点
        var sourceX = 0;
        var sourceY = 0;

        var layerIndex = layer;
        var layerName = "layer";

        //鼠标点击按下事件，画图准备
        canvas.onmousedown = function (e) {

            //设置画笔颜色和宽度
            var color = that.penColor;
            // var width = that.penWidth;

            //设置原点坐标
            sourceX = e.clientX - canvasLeft;
            sourceY = e.clientY - canvasTop;

            //鼠标移动事件，画图
            canvas.onmousemove = function (e) {

                layerIndex++;
                layer++;
                layerName += layerIndex;
                //当前坐标
                var currX = e.clientX - canvasLeft;
                var currY = e.clientY - canvasTop;

                //画线
                $("#" + canvasId).drawLine({
                    layer: true,
                    name: layerName,
                    strokeStyle: color,
                    // strokeWidth: width,
                    x1: sourceX,
                    y1: sourceY,
                    x2: currX,
                    y2: currY
                });

                //设置原点坐标
                sourceX = currX;
                sourceY = currY;
            }
        }
        //鼠标没有按下了，画图结束
        canvas.onmouseup = function (e) {
                $("#" + canvasId).drawLayers().saveCanvas();
                canvas.onmousemove = null;
            },
            function (penColor) {
                this.penColor = penColor;
            },
            function (width) {
                this.penWidth = width;
            }

    }
}