var SDK = /** @class */ (function () {
    function SDK() {
        this.url = "http://127.0.0.1:8000/api/";
        this.register_url = "register/";
        this.register_app_url = "users/apps/";
    }
    SDK.prototype.register = function (username, password, first_name, email) {
        var data = new URLSearchParams();
        data.append("password", password);
        data.append("password2", password);
        data.append("username", username);
        data.append("first_name", first_name);
        data.append("email", email);
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
    SDK.prototype.register_app = function (username, password) {
        fetch(this.url + this.register_app_url, {
            method: "POST",
            headers: {
                Authorization: "Basic " + btoa("".concat(username, ":").concat(password)),
            },
        })
            .then(function (response) { return response.json(); })
            .then(function (data) {
            console.log(JSON.stringify(data));
        });
    };
    return SDK;
}());
var sdk = new SDK();
//sdk.register("venom", "123", "venom", "venom@gmail.com");
sdk.register_app("venom", "123");
