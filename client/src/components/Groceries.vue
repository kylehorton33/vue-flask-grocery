<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Groceries</h1>
        <br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.item-modal>Add Item</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Item</th>
              <!-- <th scope="col">Category</th> -->
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in items" :key="index">
              <td>{{ item.name }}</td>
              <!-- <td>{{ item.category }}</td> -->
              <td class="text-right">
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.item-update-modal
                          @click="editItem(item)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteItem(item)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addItemModal"
            id="item-modal"
            title="Add a new item"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addItemForm.name"
                        required
                        placeholder="Enter item">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-category-group"
                      label="Category:"
                      label-for="form-category-input">
            <b-form-input id="form-category-input"
                          type="text"
                          v-model="addItemForm.category"
                          required
                          placeholder="Enter category">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editItemModal"
            id="item-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-name-edit-group"
                    label="Name:"
                    label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-category-edit-group"
                      label="Category:"
                      label-for="form-category-edit-input">
            <b-form-input id="form-category-edit-input"
                          type="text"
                          v-model="editForm.category"
                          required
                          placeholder="Enter category">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

const API = process.env.VUE_APP_API_URL || 'http://localhost:5000';

export default {
  data() {
    return {
      items: [],
      addItemForm: {
        name: '',
        category: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        name: '',
        category: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getItems() {
      const path = `${API}/items`;
      axios.get(path)
        .then((res) => {
          this.items = res.data.items;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addItem(payload) {
      const path = `${API}/items`;
      axios.post(path, payload)
        .then(() => {
          this.getItems();
          this.message = 'Item added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getItems();
        });
    },
    initForm() {
      this.addItemForm.name = '';
      this.addItemForm.category = '';
      this.editForm.id = '';
      this.editForm.name = '';
      this.editForm.category = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addItemModal.hide();
      const payload = {
        name: this.addItemForm.name,
        category: this.addItemForm.category,
      };
      this.addItem(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addItemModal.hide();
      this.initForm();
    },
    editItem(item) {
      this.editForm = item;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      const payload = {
        name: this.editForm.name,
        category: this.editForm.category,
      };
      this.updateItem(payload, this.editForm.id);
    },
    updateItem(payload, itemID) {
      const path = `${API}/items/${itemID}`;
      axios.put(path, payload)
        .then(() => {
          this.getItems();
          this.message = 'Item updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getItems();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editItemModal.hide();
      this.initForm();
      this.getItems(); // why?
    },
    removeItem(itemID) {
      const path = `${API}/items/${itemID}`;
      axios.delete(path)
        .then(() => {
          this.getItems();
          this.message = 'Item removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getItems();
        });
    },
    onDeleteItem(item) {
      this.removeItem(item.id);
    },
  },
  created() {
    this.getItems();
  },
};
</script>
