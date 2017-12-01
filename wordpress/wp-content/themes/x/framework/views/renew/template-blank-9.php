<?php

// =============================================================================
// VIEWS/RENEW/TEMPLATE-BLANK-9.PHP (Custom Ting)
// -----------------------------------------------------------------------------
// A blank page for creating unique layouts.
// =============================================================================

?>

<?php get_header(); ?>

  <div class="x-main full" role="main">

    <?php while ( have_posts() ) : the_post(); ?>

      <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
        <?php x_get_view( 'global', '_content', 'the-content' ); ?>
        <div class="x-column x-sm cs-ta-center x-1-1" style="padding: 0px;"><a class="x-btn x-btn-global" href="#" data-options="thumbnail: ''">Submit</a></div>
        <br><br><br><br>
      </article>

    <?php endwhile; ?>

  </div>

<?php get_footer(); ?>