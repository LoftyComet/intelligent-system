
function optBtnHandler(e){
    var optType = $(this).attr("opttype");
    var dataId = $(this).attr("dataId");
    if(optType == "editUser"){
        var username = $(this).attr("username");
        $("#edit_user_id").val(dataId);
        $("#edit_user_fullname").val(username);
        var myModal = new bootstrap.Modal(document.getElementById('edit_user_modal'), {
          keyboard: false
        });
        myModal.show();
    }
    else if(optType == "deleteUser"){
        var username = $(this).attr("username");
        var isconfirm = confirm("您确定删除用户“"+username+"”吗？")
        if(isconfirm){
            $.post('/user',
                {
                    "type": 'delete',
                    "id":dataId
                },
                function (callback) {
                    window.location.reload();
                })
        }
    }
    else if(optType == "editCar"){
        // console.log("111");
        var light = $(this).attr("light");
        var traffic = $(this).attr("traffic");
        var time = $(this).attr("time");
        $("#edit_car_id").val(dataId);
        $("#edit_car_light").val(light);
        $("#edit_car_traffic").val(traffic);
        $("#edit_car_time").val(time);
        var myModal = new bootstrap.Modal(document.getElementById('edit_car_modal'), {
          keyboard: false
        });
        myModal.show();
        }
    else if(optType == "deleteCar"){
        var time = $(this).attr("time");
        $("#edit_car_id").val(dataId);
        var isconfirm = confirm("您确定删除“"+time+"”时段的车流量记录吗？")
        if(isconfirm){
            $.post('/car',
                {
                    "type": 'delete',
                    "id":dataId
                },
                function (callback) {
                    window.location.reload();
                })
        }
    }
    else if(optType=="editRule"){
        
        var condition = $(this).attr("condition");
        var conclusion = $(this).attr("conclusion");
        var threhold = $(this).attr("threshold");
        var updater = $(this).attr("updater");
        var updateTime = $(this).attr("updateTime");
        $("#edit_rule_id").val(dataId);
        $("#edit_rule_condition").val(condition);
        $("#edit_rule_conclusion").val(conclusion);
        $("#edit_rule_threshold").val(threhold);
        $("#edit_rule_updater").val(updater);
        $("#edit_rule_updateTime").val(updateTime);
        var myModal = new bootstrap.Modal(document.getElementById('edit_rule_modal'), {
          keyboard: false
        });
        myModal.show();
    }
    else if(optType == "deleteRule"){
        var time = $(this).attr("time");
        $("#edit_rule_id").val(dataId);
        var isconfirm = confirm("您确定删除这条知识吗？")
        if(isconfirm){
            $.post('/rule',
                {
                    "type": 'delete',
                    "id":dataId
                },
                function (callback) {
                    window.location.reload();
                })
        }
    }
    else if(optType=="editRule2"){
        // console.log("添加了");
        var condition = $(this).attr("condition");
        var conclusion = $(this).attr("conclusion");
        var threhold = $(this).attr("threshold");
        var yuzhi = $(this).attr("yuzhi");
        var updater = $(this).attr("updater");
        var updateTime = $(this).attr("updateTime");
        $("#edit_rule2_id").val(dataId);
        $("#edit_rule2_condition").val(condition);
        $("#edit_rule2_conclusion").val(conclusion);
        $("#edit_rule2_threshold").val(threhold);
        $("#edit_rule2_yuzhi").val(yuzhi);
        $("#edit_rule2_updater").val(updater);
        $("#edit_rule2_updateTime").val(updateTime);
        var myModal = new bootstrap.Modal(document.getElementById('edit_rule2_modal'), {
          keyboard: false
        });
        myModal.show();
    }
}

function onAddUserClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_user_modal'), {
      keyboard: false
    })
    myModal.show()
}

function onAddUserSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_user_modal_show_btn'), {
      keyboard: false
    })
    var fullname = $("#fullname").val();
    $.post('/user',
        {
            "type": 'add',
            "username": $("#fullname").val()
        },
        function (callback) {
            window.location.reload();
        })
    myModal.hide()
}


function onEidtUserSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_user_modal_show_btn'), {
      keyboard: false
    })
    var fullname = $("#edit_user_fullname").val();
    var id = $("#edit_user_id").val();
    $.post('/user',
        {
            "type": 'edit',
            "username": fullname,
            "id":id
        },
        function (callback) {
            window.location.reload();
        })


    myModal.hide()
}

// 下面是车流量的增删改查
function onAddCarClickHandler(e){
    // console.log("我被点击了");
    var myModal = new bootstrap.Modal(document.getElementById('add_car_modal'), {
      keyboard: false
    })
    myModal.show()
}

function onAddCarSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_car_modal_show_btn'), {
      keyboard: false
    })
    // topRight,eastLeft,eastRight,topLeft
    var light = $("#add_car_light").val();
    var topRight = $("#add_car_topRight").val();
    var eastLeft = $("#add_car_eastLeft").val();
    var eastRight = $("#add_car_eastRight").val();
    var topLeft = $("#add_car_topLeft").val();
    var time = $("#add_car_time").val();
    console.log("点击了添加");
    $.post('/car',
        {
            "type": 'add',
            "light": light,
            "topRight": topRight,
            "eastLeft": eastLeft,
            "topLeft": topLeft,
            "eastRight": eastRight,
            "time": time,
        },
        function (callback) {
            window.location.reload();
        })


    myModal.hide()
}

function onEidtCarSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_car_modal_show_btn'), {
      keyboard: false
    })
    var light = $("#edit_car_light").val();
    var traffic=$("#edit_car_traffic").val();
    var time=$("#edit_car_time").val();
    var id = $("#edit_car_id").val();
    $.post('/car',
        {
            "type": 'edit',
            "light": light,
            "traffic": traffic,
            "time": time,
            "id":id
        },
        function (callback) {
            window.location.reload();
        })
    myModal.hide()
}


// 下面是模糊知识的增删改查
function onAddRuleClickHandler(e){
    // console.log("我被点击了");
    var myModal = new bootstrap.Modal(document.getElementById('add_rule_modal'), {
      keyboard: false
    })
    // alert("cjdsb");
    myModal.show()
}

function onAddRuleSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_rule_modal_show_btn'), {
      keyboard: false
    })
    var condition=$("#add_rule_condition").val();
    var conclusion=$("#add_rule_conclusion").val();
    var threshold=$("#add_rule_threshold").val();
    var updater=$("#add_rule_updater").val();
    var updateTime=$("#add_rule_updateTime").val();
    $.post('/rule',
        {
            "type": 'add',
            "condition": condition,
            "conclusion": conclusion,
            "threshold": threshold,
            "updater": updater,
            "updateTime": updateTime,

        },
        function (callback) {
            window.location.reload();
        })


    myModal.hide()
}

function onEidtRuleSubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_rule_modal_show_btn'), {
      keyboard: false
    })
    var condition=$("#edit_rule_condition").val();
    // console.log(conclusion)
    var conclusion=$("#edit_rule_conclusion").val();
    var threshold=$("#edit_rule_threshold").val();
    console.log("threshold");
    console.log(threshold);
    var updater=$("#edit_rule_updater").val();
    var updateTime=$("#edit_rule_updateTime").val();
    var id=$("#edit_rule_id").val();
    console.log(id);
    $.post('/rule',
        {
            "type": 'edit',
            "condition": condition,
            "conclusion": conclusion,
            "threshold": threshold,
            "updater": updater,
            "updateTime": updateTime,
            "id":id
        },
        function (callback) {
            window.location.reload();
        })
    myModal.hide()
}

// 下面是可信度知识的增删改查
function onAddRule2ClickHandler(e){
    // alert("我被点击了");
    console.log("我被点击了");
    var myModal = new bootstrap.Modal(document.getElementById('add_rule2_modal'), {
      keyboard: false
    })
    myModal.show()
}

function onAddRule2SubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_rule2_modal_show_btn'), {
      keyboard: false
    })
    var condition=$("#add_rule2_condition").val();
    var conclusion=$("#add_rule2_conclusion").val();
    var threshold=$("#add_rule2_threshold").val();
    var yuzhi=$("#add_rule2_yuzhi").val();
    var updater=$("#add_rule2_updater").val();
    var updateTime=$("#add_rule2_updateTime").val();
    $.post('/rule2',
        {
            "type": 'add',
            "condition": condition,
            "conclusion": conclusion,
            "threshold": threshold,
            "yuzhi":yuzhi,
            "updater": updater,
            "updateTime": updateTime,

        },
        function (callback) {
            window.location.reload();
        })


    myModal.hide()
}

function onEidtRule2SubmitClickHandler(e){
    var myModal = new bootstrap.Modal(document.getElementById('add_rule2_modal_show_btn'), {
      keyboard: false
    })
    var condition=$("#edit_rule2_condition").val();
    // console.log(conclusion)
    var conclusion=$("#edit_rule2_conclusion").val();
    var threshold=$("#edit_rule2_threshold").val();
    var yuzhi=$("#edit_rule2_yuzhi").val();
    console.log("threshold");
    console.log(threshold);
    var updater=$("#edit_rule2_updater").val();
    var updateTime=$("#edit_rule2_updateTime").val();
    var id=$("#edit_rule2_id").val();
    console.log(id);
    $.post('/rule2',
        {
            "type": 'edit',
            "condition": condition,
            "conclusion": conclusion,
            "threshold": threshold,
            "yuzhi":yuzhi,
            "updater": updater,
            "updateTime": updateTime,
            "id":id
        },
        function (callback) {
            window.location.reload();
        })
    myModal.hide()
}





$(document).ready(function(){
    $('#add_user_modal_show_btn').click(onAddUserClickHandler);
    $("#add_user_submit").click(onAddUserSubmitClickHandler);
    $("#edit_user_submit").click(onEidtUserSubmitClickHandler);
    $(".optbtn").click(optBtnHandler);


    $("#edit_car_submit").click(onEidtCarSubmitClickHandler);
    $('#add_car_modal_show_btn').click(onAddCarClickHandler);
    $("#add_car_submit").click(onAddCarSubmitClickHandler);

    $("#edit_rule_submit").click(onEidtRuleSubmitClickHandler);
    $('#add_rule_modal_show_btn').click(onAddRuleClickHandler);
    $("#add_rule_submit").click(onAddRuleSubmitClickHandler);

    $("#edit_rule2_submit").click(onEidtRule2SubmitClickHandler);
    $('#add_rule2_modal_show_btn').click(onAddRule2ClickHandler);
    $("#add_rule2_submit").click(onAddRule2SubmitClickHandler);


})

