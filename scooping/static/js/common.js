<<<<<<< HEAD
        /**
         * 创建函数 - createXhr
         * 目的:为了根据不同的浏览器创建不同的异步对象
         * 返回值:创建好的异步对象
         */
         function createXhr(){
            if(window.XMLHttpRequest){
                //创建XMLHttpRequest的对象并返回
                return new XMLHttpRequest();
            }else{
                //创建ActiveXObject的对象并返回
                return new ActiveXObject("Microsoft.XMLHTTP");
            }
         }
=======
function createXhr(){
            if(window.XMLHttpRequest){
                return new XMLHttpRequest();
                }else{
                return new ActiveXObject("Microsoft.XMLHTTP");
                }
        }
>>>>>>> 8cd4fb14074657d9adc0d266feb5a878d46cd931
