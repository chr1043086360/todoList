/* eslint-disable no-console */
<template>
  <el-card class="box-card">
    <!-- gutter:栅格间隔 -->
    <el-row :gutter="30">
      <!-- span:栅格占的列数, offset:栅格左侧间隔数 -->
      <el-col :span="16" :offset="2">
        <el-input v-model="newTitle" size placeholder="请输入待办事项..." />
      </el-col>
      <el-col :span="6">
        <el-button type="primary" icon="el-icon-plus" @click="handleAdd" circle></el-button>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <el-table :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
      <el-table-column type="index" width="50"></el-table-column>
      <el-table-column align="center" label="待办事项" prop="Title"></el-table-column>
      <el-table-column align="right" label="操作">
        <template slot-scope="scope">
          <!-- {{scope.row.ID}} -->
          <!-- {{scope.row.Status}} -->
          <el-button
            type="success"
            icon="el-icon-check"
            v-show="scope.row.Status"
            @click="handleEdit(scope.$index, scope.row)"
            circle
          ></el-button>
          <el-button
            type="warning"
            icon="el-icon-refresh-left"
            v-show="!scope.row.Status"
            @click="handleEdit(scope.$index, scope.row)"
            circle
          ></el-button>
          <el-button
            type="danger"
            icon="el-icon-close"
            @click="handleDelete(scope.$index, scope.row.ID)"
            circle
          ></el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-card>
</template>

<script>
export default {
  name: "TodoList",
  data() {
    return {
      tableData: [],
      newTitle: ""
    };
  },
  mounted() {
    this.axios
      .get("/api/v3/todo")
      .then(response => (this.tableData = response.data.data));
  },
  methods: {
    tableRowClassName({ row }) {
      if (row.Status) {
        return "success-row";
      } else {
        return "";
      }
    },
    getTodoList() {
      this.axios
        .get("/api/v3/todo")
        .then(response => (this.tableData = response.data.data));
    },
    handleEdit(index, row) {
      let messageSuffix = row.Status ? " 置为未完成" : " 置为已完成";
      this.axios
        .put("/api/v3/todo/" + row.ID, {
          status: !row.Status
        })
        .then(() => {
          this.tableData[index].Status = !row.Status;
          this.$message({
            showClose: true,
            duration: 1500,
            message: `<${row.Title}> ${messageSuffix}`,
            type: "success"
          });
        });
    },
    handleDelete(index, rowId) {
      this.axios.delete("/api/v3/todo/" + rowId).then(() => {
        this.tableData.splice(index, 1); // 删除index行元素
        this.$message({
          showClose: true,
          duration: 1500,
          message: "删除待办事项成功",
          type: "success"
        });
      });
    },
    handleAdd() {
      if (this.newTitle != "") {
        this.axios
          .post("/api/v3/todo", {
            title: this.newTitle
          })
          .then(() => {
            this.getTodoList();
            this.$message({
              showClose: true,
              duration: 1500,
              message: "添加待办事项成功",
              type: "success"
            });
          });
        this.newTitle = "";
      } else {
        this.$message({
          showClose: true,
          duration: 1500,
          message: "title不能为空哦",
          type: "warning"
        });
      }
    }
  }
};
</script>

<style>
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  text-decoration: line-through;
}
</style>