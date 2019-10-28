$( document ).ready(function() {
    var timers = [];
    var modal = $("#resultModal");

    var modalTitle = $(".modalTitle");
    var userModalChoiceText = $("#userText.modalChoiceText");
    var curbModalChoiceText = $("#curbText.modalChoiceText");
    var modalUserImage = $(".modalUserImage");
    var modalCurbImage = $(".modalCurbImage");
    var modalExplanationText = $(".modalExplanationText");
    var confirmBtn = $(".confirmBtn");
    var displayUserChoice = $("#userChoice.modalChoiceContainer")
    var displayCurbChoice = $("#curbChoice.modalChoiceContainer")

    function populateModal(userChoice){
        userModalChoiceText.attr("hidden", false);
        curbModalChoiceText.attr("hidden", false);
        modalUserImage.attr("hidden", false);
        modalCurbImage.attr("hidden", false);
        confirmBtn.attr("hidden", true);
        displayUserChoice.attr("hidden", false);
        displayCurbChoice.attr("hidden", false);
        modalTitle.text("WAITING CURB'S CHOICE");
        userModalChoiceText.text(userChoice);
        modalUserImage.attr("src", "static/img/"+userChoice.charAt(0).toLowerCase()+userChoice.slice(1)+".png");
        modalCurbImage.attr("src", "static/img/wait.png");
        modalExplanationText.attr("hidden", true);

        timers.push(setTimeout(() => {
            $.post('/game', { userChoice: userChoice }).done((response)=>{
                console.log(response);
                var curbChoice = response.curbChoice;
                var result = response.result;
                (result!=="UNDEFINED") ? modalCurbImage.attr("src", "static/img/"+curbChoice.charAt(0).toLowerCase()+curbChoice.slice(1)+".png") : null;
                curbModalChoiceText.text(curbChoice);
                timers.push(setTimeout(()=>{

                    modalTitle.text(result);
                    modalExplanationText.attr("hidden", false);
                    confirmBtn.attr("hidden", false)
                    if (result === "YOU LOST"){
                        modalExplanationText.text("Curb with " + curbChoice + " wins");
                        userModalChoiceText.attr("hidden", true)
//                        modalUserImage.attr("hidden", true)
                        displayCurbChoice.attr("hidden", true);
                    } else if (result === "YOU WIN"){
                        modalExplanationText.text("You win with " + userChoice);
                        curbModalChoiceText.attr("hidden", true)
//                        modalCurbImage.attr("hidden", true)
                        displayUserChoice.attr("hidden", true);
                    } else if (result === "UNDEFINED"){
                        modalExplanationText.text("Invalid Choice");
                        modalTitle.text("Invalid Choice from Curb");
                    }
                }, 1500));
            }).fail(() =>{
                curbModalChoiceText.text("Cannot Reach the server");
                confirmBtn.attr("hidden", false)
            });
        }, 1500));

    };
    $(".selectionBtn").click(function (){

        var selectedItemStr = $(this).text();
        populateModal(selectedItemStr);

        modal.modal();
    });

    modal.on('hide.bs.modal', function (e) {
        for (var i = 0; i < timers.length; i++)
        {
            clearTimeout(timers[i]);
        }
    })


});