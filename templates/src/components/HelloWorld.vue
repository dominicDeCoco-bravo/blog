<template>
  <div class="hello">
      <div id="content">
    
        <div v-for="com in comments">
          
            <p>{{com.text}}
              <button @click='deleteComment(com.id)'>Удалить</button>
               </p>
        </div> 
       
      </div>
    
      <div id="footer">
        <p><textarea cols="70" placeholder="Введите комментарий" v-model="text"></textarea>
        <button @click="add()">Добавить</button></p>
      </div>
    
    </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      comments: [
        {
          id: 1,
          text: "qwerty"
        },
        {
          id: 2,
          text: "qwerty"
        }
      ],
      text: ""
    };
  },
  mounted() {
    this.loadComments();
  },
  methods: {
    loadComments() {
      var url = "http://localhost:5000/list";
      var xhr = new XMLHttpRequest();
      xhr.open("GET", url, true);
      xhr.onload = () => {
        var comments = JSON.parse(xhr.responseText);
        if (xhr.readyState == 4 && xhr.status == "200") {
          console.log("response", comments);
          this.comments = comments;
        } else {
          console.error(users);
        }
      };
      xhr.send(null);
    },
    add() {
      var url = "http://localhost:5000/add";

      var json = JSON.stringify({text: this.text});

      var xhr = new XMLHttpRequest();
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-type", "application/json; charset=utf-8");
      xhr.onload = () => {
       
        if (xhr.readyState == 4 && xhr.status == "200") {
          this.loadComments();
            } 
      };
      this.text="";
      xhr.send(json);
    },
    deleteComment(id) {
      var url = "http://localhost:5000/delete";
      var xhr = new XMLHttpRequest();
      xhr.open("DELETE", url + "/" + id, false);
      xhr.onload = () => {
        if (xhr.readyState == 4 && xhr.status == "200") {
          this.loadComments();
        } 
      };
      xhr.send(null);
    }
  }
};
</script>
