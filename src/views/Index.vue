/* eslint-disable no-console */
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
      <el-button class="log_out" @click="logout" type="primary" icon="el-icon-switch-button">EXIT</el-button>

      <div class="myPlans">
        <a href="http://122.51.107.26:5555">My Plans</a>
      </div>
    </el-header>
    <!-- {{tableData}} -->
    <!-- <el-button class="myHome_btn" type="primary" icon="el-icon-edit" circle></el-button> -->

    <el-form
      v-if="status"
      :model="loginForm"
      status-icon
      :rules="rules"
      ref="loginForm"
      class="demo-ruleForm"
    >
      <el-form-item prop="username">
        <el-input
          type="text"
          v-model="loginForm.username"
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
        <!-- 注册 -->
        <el-button type="danger" @click="submitForm('loginForm', 1)" class="reg-btn">注册</el-button>

        <!-- 登录 -->
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
import router from "../router/index";
export default {
  name: "Index",
  components: {
    TodoList
  },
  data() {
    var validateUsername = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账号"));
      } else {
        if (this.loginForm.username !== "") {
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
      tableData: [],
      loginForm: {
        username: "",
        password: ""
      },
      rules: {
        username: [
          {
            validator: validateUsername,
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
    // 控制是否显示登录注册模块
    showLogin() {
      this.status = !this.status;
    },
    submitForm(formName, type) {
      // let that = this;
      if (type === 1) {
        this.axios
          // 注册接口
          .post("/api/v3/register", {
            username: this.loginForm.username,
            password: this.loginForm.password
          })
          .then(response => {
            if (response.data.code === 200) {
              this.$message({
                showClose: true,
                duration: 1500,
                message: "注册成功",
                type: "success"
              });
            } else {
              this.$message({
                showClose: true,
                duration: 2000,
                message: "该用户名已经有人注册!",
                type: "error"
              });
            }
          });
      }
      // 登录接口
      if (type === 2) {
        this.axios
          .post("/api/v3/login", {
            username: this.loginForm.username,
            password: this.loginForm.password
          })
          .then(response => {
            this.tableData = response.data;
            if (this.tableData.data === 50001) {
              this.$message({
                showClose: true,
                duration: 2000,
                message: "用户未注册,请先注册!",
                type: "warning"
              });
            } else if (this.tableData.data === 40001) {
              this.$message({
                showClose: true,
                duration: 2000,
                message: "请输入正确的用户名或密码!",
                type: "error"
              });
            } else {
              // this.status = !this.status;
              // 刷新界面
              router.go(0);
              // this.axios.get("/api/v3/todo");
              // setTimeout()
              this.$message({
                showClose: true,
                duration: 2500,
                message: "主人,欢迎回家!",
                type: "success"
              });
            }
          });
      }
    },
    // 退出登录接口
    logout() {
      this.axios.get("/api/v3/logout").then(response => {
        if (response.data.data === 403) {
          this.$message({
            showClose: true,
            duration: 1500,
            message: "您还没有登录哦,主人!",
            type: "warning"
          });
        } else if (response.data.data === 200) {
          router.go(0);
          this.$message({
            showClose: true,
            duration: 2500,
            message: "欢迎下次光临!",
            type: "success"
          });
        }
      });
    }
  }
};
</script>
<style>
.el-button.myHome_btn.el-button--primary {
  margin-top: 10px;
  margin-left: 10px;
}
.el-button.log_out.el-button--primary {
  margin-right: 12px;
  margin-top: 14px;
  padding: 7px;
}
.el-button.log_out.el-button--primary span {
  font-size: 18px;
}

.el-icon-switch-button {
  font-size: 18px;
}
.myHome_btn {
  /* position: fixed; */
  /* top: 10px; */
  /* left: 10px; */
  float: left;
  /* margin-left: 0px;
  font-size: 30px; */
}
.log_out {
  float: right;
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
.myPlans a {
  display: block;
  text-decoration: none;
  color: hsl(356, 81%, 59%);
  text-align: center;
  /* position: absolute; */
  width: 160px;
  margin: 0 auto;
  font-weight: 600;
}
.el-button.myHome_btn.el-button--primary span {
  font-size: 18px;
}
.el-button.myHome_btn.el-button--primary {
  background: #f3f3f399;
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