<template>
  <el-container>
    <el-header>My Plans</el-header>
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

export default {
  name: "Index",
  components: {
    TodoList
  }
};
</script>
<style>
.el-header {
  background-color: #409eff;
  color: #fff;
  text-align: center;
  line-height: 60px;
  /* word-spacing: 0.1px; */
  /* letter-spacing: 1px; */
  font-weight: 900;
  font-style: italic;
  font-size: 30px
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