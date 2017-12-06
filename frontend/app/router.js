import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.baseURL
});

Router.map(function() {
  this.route('about');
  this.route('contact');
  this.route('menu');
  this.route('home');
  this.route('login');
  this.route('checkout');
});

export default Router;
