const gulp = require('gulp');
const mjml = require('gulp-mjml');

gulp.task('default', function() {
  return gulp.src('./assets/mjml/*.mjml')
    .pipe(mjml())
    .pipe(gulp.dest('./templates/registration'))
})
