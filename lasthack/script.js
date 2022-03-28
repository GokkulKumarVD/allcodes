

let correctAnswer = ['C', 'C', 'D', 'D', 'D', 'A', 'D', 'D', 'A', 'A'];
console.log('working')
let form = document.querySelector('.quiz-form');
let result = document.querySelector('.result');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  result.style.display = 'block';

  let score = 0;

  let userAnswer = [form.opt.value,
    form.opt1.value, form.opt2.value, form.opt3.value, form.opt4.value, form.opt5.value, form.opt6.value, form.opt7.value,
    form.opt8.value, form.opt9.value
  ];
  console.log(userAnswer)

  userAnswer.forEach((element, index) => {
    if (element === correctAnswer[index]) {
      score += 1;
    }
  });
  console.log(score);

  scrollTo(0, 0);
  result.classList.remove('d-none');

  let output = 0;
  let tm = setInterval(() => {
    result.querySelector('span').textContent = `${output}/10`;
    if (output === score) {
      clearInterval(tm);
    } else {
      output++;
    }

  }, 100)



  // ----------------------------------------------------------------

  var emailid = '<?php echo $session_value; ?>';
  var starttime = '<?php echo $starttime; ?>';
  console.log(emailid);
  console.log('starttime');




  $(function() {
    console.log(emailid);
    console.log(score);
    if (emailid === null ||
      emailid === undefined) {
      alert('Enter all the fields');
    } else {
      $.get('insertscore.php', {
        'emailid': emailid,
        'score': score,
        'starttime': starttime
      }, function() {
        console.log('worked');

      }, "json");

    }

  });

//   window.setTimeout(function() {
//     window.location.href = "http://www.infoquiz.swiggy.in/";
//   }, 3000);

});
