var SDK = /** @class */ (function () {
    function SDK(username, password, first_name, email) {
        this.url = "http://127.0.0.1:8000/api/";
        this.register_url = "register/";
        this.register_app_url = "users/apps/";
        this.users_to_app_url = "users/apps/users/user/";
        this.username = username;
        this.password = password;
        this.first_name = first_name;
        this.email = email;
    }
    SDK.prototype.register = function () {
        var data = new URLSearchParams();
        data.append("password", this.password);
        data.append("password2", this.password);
        data.append("username", this.username);
        data.append("first_name", this.first_name);
        data.append("email", this.email);
        fetch(this.url + this.register_url, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: data.toString(),
            // mode: "cors",
        })
            .then(function (response) { return response.json(); })
            .then(function (data) {
            console.log(JSON.stringify(data));
        });
    };
    SDK.prototype.register_app = function () {
        fetch(this.url + this.register_app_url, {
            method: "POST",
            headers: {
                Authorization: "Basic " + btoa("".concat(this.username, ":").concat(this.password)),
            },
        })
            .then(function (response) { return response.json(); })
            .then(function (data) {
            console.log(JSON.stringify(data));
        });
    };
    SDK.prototype.add_users_to_app = function (app_id, user) {
        var data = new URLSearchParams();
        data.append("app_id", app_id);
        data.append("username", user);
        fetch(this.url + this.users_to_app_url, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                Authorization: "Basic " + btoa("".concat(this.username, ":").concat(this.password)),
            },
            body: data.toString(),
        })
            .then(function (response) { return response.json(); })
            .then(function (data) {
            console.log(JSON.stringify(data));
        });
    };
    return SDK;
}());
var sdk = new SDK("venom", "123", "venom", "venom@gmail.com");
// sdk.register();
// sdk.register_app();
sdk.add_users_to_app("2", "batman");
