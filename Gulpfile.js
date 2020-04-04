const del = require('del');
const gulp = require('gulp');
const mjml = require('gulp-mjml');

function clean() {
  return del([ 'dist' ]);
}

function emails() {
  return gulp.src('./assets/src/mjml/*.mjml')
    .pipe(mjml())
    .pipe(gulp.dest('./templates/email/'))
}

var build = gulp.series(clean, emails)

exports.clean = clean;
exports.emails = emails;

exports.default = build;
