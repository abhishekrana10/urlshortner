setInterval(function () {
                    var $badge = $('#time');
                    var value = parseInt($badge.html());
                    value--;
                    if(value == 0){
                    var x=document.getElementById("before_timeout");
                    var y=document.getElementById("after_timeout");
                    x.style.display="none";
                    y.style.display="block";
                    }
                    $badge.html(value);
               }, 1000);

function copyToClipboard(element) {
            var $temp = $("<input>");
            $("body").append($temp);
            $temp.val($(element).text()).select();
            document.execCommand("copy");
            $temp.remove();
            }

function selectText(containerid) {
        if (document.selection) {
            var range = document.body.createTextRange();
            range.moveToElementText(document.getElementById(containerid));
            range.select();
        } else if (window.getSelection) {
            var range = document.createRange();
            range.selectNode(document.getElementById(containerid));
            window.getSelection().removeAllRanges();
            window.getSelection().addRange(range);
        }
    }