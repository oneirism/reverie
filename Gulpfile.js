const gulp = require('gulp');

const css = require('gulp-clean-css');
const mjml = require('gulp-mjml');

gulp.task('emails', function() {
  return gulp.src('./assets/src/mjml/*.mjml')
    .pipe(mjml())
    .pipe(gulp.dest('./templates/email/'))
});

gulp.task('css', function() {
  return gulp.src('./assets/src/css/*.css')
    .pipe(css())
    .pipe(gulp.dest('./assets/dist/css/'))
});

gulp.task('default', ['emails', 'css']);
