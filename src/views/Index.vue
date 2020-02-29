<template>
  <el-container>
    <el-header>
      <el-button
        class="myHome_btn"
        @click="showLogin"
        type="primary"
        icon="el-icon-s-custom
"
        circle
      ></el-button>
      <div class="myPlans">My Plans</div>
    </el-header>

    <!-- <el-button class="myHome_btn" type="primary" icon="el-icon-edit" circle></el-button> -->

    <el-form
      v-if="status"
      :model="loginForm"
      status-icon
      :rules="rules"
      ref="loginForm"
      class="demo-ruleForm"
    >
      <el-form-item prop="userName">
        <el-input
          type="text"
          v-model="loginForm.userName"
          autocomplete="off"
          placeholder="Username"
          class="fuck"
        ></el-input>
      </el-form-item>
      <el-form-item prop="password" @keyup.enter.native="submitForm('loginForm')" inline="true">
        <el-input
          type="password"
          v-model="loginForm.password"
          autocomplete="off"
          placeholder="Password"
        ></el-input>
      </el-form-item>
      <el-form-item class="btn_login_form">
        <el-button type="danger" @click="submitForm('loginForm', 1)" class="reg-btn">注册</el-button>
        <el-button
          type="primary"
          @click="submitForm('loginForm', 2)"
          style="margin-top: 10px; margin-left: 200"
          class="login-btn"
        >登录</el-button>
      </el-form-item>
    </el-form>
    <el-main>
      <el-row type="flex" justify="center">
        <el-col :xs="20" :span="12">
          <div class="grid-content">
            <el-divider>
              <h1>我的清单</h1>
            </el-divider>
            <TodoList></TodoList>
          </div>
        </el-col>
      </el-row>
    </el-main>
    <!-- <el-radio-group v-model="direction"> :before-close="handleClose"
      <el-radio label="ltr">从左往右开</el-radio>
    </el-radio-group>-->
    <!-- <el-drawer :visible.sync="drawer" :direction="direction"> -->
    <!-- <div class="block">
        <el-avatar :size="100" :src="circleUrl"></el-avatar>
    </div>-->
    <!-- </el-drawer> -->
    <el-footer>
      Welcome To My
      <a href="https://github.com/chr1043086360">Github</a> and
      <a href="https://blog.csdn.net/qq_44291044">Blog</a>
    </el-footer>
  </el-container>
</template>

<script>
// @ is an alias to /src
import TodoList from "@/components/TodoList.vue";
// import { post_login, post_register } from '@/server/api/server';
export default {
  name: "Index",
  components: {
    TodoList
  },
  data() {
    var validateUserName = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账号"));
      } else {
        if (this.loginForm.userName !== "") {
          // this.$refs.loginForm.validateField('userName');
        }
        callback();
      }
    };
    var validatePassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.loginForm.password !== "") {
          // this.$refs.loginForm.validateField('password');
        }
        callback();
      }
    };
    return {
      loginForm: {
        userName: "",
        password: ""
      },
      rules: {
        userName: [
          {
            validator: validateUserName,
            trigger: "blur"
          }
        ],
        password: [
          {
            validator: validatePassword,
            trigger: "blur"
          }
        ]
      },
      // 是否显示登录框
      status: false
    };
  },
  methods: {
    showLogin() {
      this.status = !this.status;
    }
    // submitForm(formName, type) {
    //   let that = this;
    //   this.$refs[formName].validate(valid => {
    //     if (valid) {
    //       // eslint-disable-next-line no-console
    //       console.log(this.loginForm.userName);
    //       // eslint-disable-next-line no-console
    //       console.log(this.loginForm.password);
    //       if (type === 1) {
    //         post_register(that.loginForm).then(res => {
    //           if (res.data.status === 1000) {
    //             this.$message({
    //               message: res.data.message,
    //               type: "success"
    //             });
    //           } else {
    //             this.$message({
    //               message: res.data.message,
    //               type: "warning"
    //             });
    //           }
    //         });
    //       } else {
    //         post_login(that.loginForm).then(res => {
    //           if (res.data.status === 1000) {
    //             this.$message({
    //               message: res.data.message,
    //               type: "success"
    //             });
    //             this.$store.dispatch("setUser", this.loginForm.userName);
    //             this.$router.push("/list");
    //           } else {
    //             this.$message({
    //               message: res.data.message,
    //               type: "warning"
    //             });
    //             this.$store.dispatch("setUser", null);
    //           }
    //         });
    //       }
    //     } else {
    //       // eslint-disable-next-line no-console
    //       console.log("error submit!!");
    //       return false;
    //     }
    //   });
    // }
  }
};
</script>
<style>
.el-button.myHome_btn.el-button--primary {
  margin-top: 10px;
  margin-left: 10px;
}
.myHome_btn {
  /* position: fixed; */
  /* top: 10px; */
  /* left: 10px; */
  float: left;
  /* margin-left: 0px;
  font-size: 30px; */
}
.btn_login_form {
  text-align: center;
}

.el-input__inner {
  text-align: center;
}
.el-form-item__error {
  text-align: center;
  position: relative !important;
  margin-top: 8px;
}
.fuck {
  margin-top: 20px;
}
.myPlans {
  text-align: center;
  /* position: absolute; */
  width: 200px;
  margin: 0 auto;
}
.el-button.myHome_btn.el-button--primary span {
  font-size: 18px;
}
.el-button.myHome_btn.el-button--primary {
  background: #ee3f4d90;
  padding: 1;
  float: left;
}
.el-header {
  /* position: fixed; */
  padding: 0 !important;
  background-color: #409eff;
  color: #fff;
  /* text-align: center; */
  line-height: 60px;
  /* word-spacing: 0.1px; */
  /* letter-spacing: 1px; */
  font-weight: 500;
  font-style: italic;
  font-size: 28px;
}
.el-footer {
  background-color: #909399;
  display: block;
  width: 100%;
  position: fixed;
  bottom: 0;
  text-align: center;
  line-height: 60px;
  color: #fff;
}
.el-footer a {
  text-decoration: none;
  color: #ee3f4d;
  margin: 0 4px;
  font-weight: 900;
  font-size: 23px;
}
.el-footer a:hover {
  /* color: rebeccapurple; */
  /* transform: scale(1.6); */
  /* color: white; */
  /* z-index: 2; */
  font-size: 30px;
  /* background: #409eff; */
  /* transition: #409eff 0.3s linear; */
  /* transform:translate(100px,100px); */
}
</style>